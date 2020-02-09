from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Create your views here.
def index(request):
    # return HttpResponse('You are at the polls index')

    latest_question_list = Question.objects.order_by('-pub_time')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    # render函数：将加载模板、传递参数，返回HttpResponse对象封装。
    # 也就是说，render函数返回一个经过字典数据渲染过的模板封装而成的HttpResponse对象。
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse('You are looking at question %s.' % question_id)
    # question = Question.objects.get(pk=question_id)  # Traceback Internal Server Error: DoesNotExist 服务器报错
    question = get_object_or_404(Question, pk=question_id)  # try ... except ... 服务器不报错
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    # response = 'You are looking at the results of question %s.'
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


# ******  使用通用视图（类视图）替代上述三个视图  ******
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_time')[:5]


class DetailView(generic.DetailView):
    # 每一种通用视图都需要知道它要作用在哪个模型上，这通过model属性提供
    # DetailView需要从url捕获到的称为"pk"的主键值，因此我们在url文件中将2和3条目的<question_id>修改成了<pk>。
    template_name = 'polls/detail.html'
    model = Question


class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question


def vote(request, question_id):
    # return HttpResponse('You are voting at question %s.' % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):  # 如果POST数据里没有提供choice键值，有可能触发一个KeyError异常
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': 'You didn\'t select a choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

        # HttpResponseRedirect需要一个参数：重定向的URL。
        # 这里有一个建议，当你成功处理POST数据后，应当保持一个良好的习惯，始终返回一个HttpResponseRedirect。
        # 这不仅仅是对Django而言，它是一个良好的WEB开发习惯。
        # reverse()函数避免在视图函数中硬编码URL