from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# Create your views here.
@login_required
def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    user = request.user

    # Check if user is allowed to comment
    if user != ticket.created_by and ticket.profile.user != user:
        return HttpResponseForbidden("You are not allowed to comment on this ticket.")


    if request.method == "POST":
        content = request.POST.get("content")
        if content:
                Comment.objects.create(ticket=ticket, user=user, content=content)
                return redirect('tickets_detail', ticket_id=ticket.id)

    return render(request, 'tickets/add_comment.html', {'ticket': ticket})