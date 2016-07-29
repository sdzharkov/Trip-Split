from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'tripapp/index.html')

@login_required
def home(request):
    #return render(request,'home.html')
    return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))
