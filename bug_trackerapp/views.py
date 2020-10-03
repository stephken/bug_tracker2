from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from bug_trackerapp.models import My_User, Ticket
from django.contrib.auth.decorators import login_required
from bug_tracker.settings import AUTH_USER_MODEL
from bug_trackerapp.forms import LoginForm, AddTicketForm, InProgressForm
# Create your views here.
