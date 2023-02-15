from django.shortcuts import render
from .models import ToDoList, ToDoItem
from django.urls import reverse, reverse_lazy

from django.views.generic import (
ListView,
CreateView,
UpdateView,
DeleteView
)

class ListListView(ListView):
    model = ToDoList
    template_name = "ToDoApp/index.html"


class ItemListView(ListView):
    model = ToDoItem
    template_name = "ToDoApp/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context


class ToDoListCreateView(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ToDoListCreateView, self).get_context_data()
        context["title"] = "Add a new list"
        return context
    def get_success_url(self):
        return reverse("index")

class ToDoItemCreateView(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ToDoItemCreateView, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ToDoItemCreateView, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("todo_list", args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("todo_list", args=[self.object.todo_list_id])


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    def get_success_url(self) -> str:
        return reverse("todo_list", args=[self.object.todo_list_id])
class ToDoListDeleteView(DeleteView):
    model = ToDoList
    def get_success_url(self) -> str:
        return reverse_lazy("index")
