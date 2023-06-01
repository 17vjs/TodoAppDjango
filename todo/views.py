from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Tag, Task
from django.shortcuts import get_object_or_404, render


def index(request):
    todo_list = Task.objects.all()
    return render(request, "todo/index.html", {
        "todo_list": todo_list,
    })
def task(request, task_id=-1):
      if task_id==-1:
        #  create task
        task={}
      else:
        try:
          task = get_object_or_404(Task, pk=task_id)
        except:
          return HttpResponse("Task does not exist")

      return render(request, "todo/detail.html", {"task": task})


def actions(request, task_id=-1):

    updatedTask=request.POST
    if 'create' in updatedTask:
      task=Task()
      task.title=updatedTask["title"]
      task.description=updatedTask["description"]
      task.due_date=updatedTask["due_date"]
      tags=updatedTask["tags"].split(",")
      task.save()

      if len(tags)!=0:
        for tag in tags:
          tag=tag.strip()
          if len(tag)!=0:
            try:
              tg=Tag.objects.get(name=tag)
            except:
              tg=Tag(name=tag)
              tg.save()

            task.tags.add(tg)
      task.save()



    if 'update' in updatedTask:
      task = get_object_or_404(Task, pk=task_id)

      task.title=updatedTask["title"]
      task.description=updatedTask["description"]
      task.due_date=updatedTask["due_date"]
      task.status=updatedTask["status"]
      for tag in task.tags.all():
        if tag.name not in updatedTask.getlist("existing_tag"):
            task.tags.remove(tag)


      tags=updatedTask["tags"].split(",")
      if len(tags)!=0:
        for tag in tags:
          tag=tag.strip()
          if len(tag)!=0:
            try:
              tg=Tag.objects.get(name=tag)
            except:
              tg=Tag(name=tag)
              tg.save()

            try:
              tg=task.tags.get(name=tag)
            except:
              task.tags.add(tg)

      task.save()
    if 'delete' in updatedTask:
      task = get_object_or_404(Task, pk=task_id)
      task.delete()


    return HttpResponseRedirect(reverse("todo:index"))

