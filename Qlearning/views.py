from django.shortcuts import render
from .ai import generate_learning_content


def home(request):
    return render(request, "index.html")


def learning(request):

    if request.method == "POST":

        topic = request.POST.get("topic")
        age = request.POST.get("age")

        try:
            lesson = generate_learning_content(topic, age)

            print("LESSON TYPE:", type(lesson))
            print("LESSON:", lesson)

            return render(
                request,
                "learning.html",
                {
                    "topic": topic,
                    "age": age,
                    "lesson": lesson,
                }
            )

        except Exception as e:

            print("AI ERROR:", e)

            return render(
                request,
                "learning.html",
                {
                    "error": str(e),
                    "topic": topic,
                    "age": age,
                }
            )

    return render(request, "learning.html")