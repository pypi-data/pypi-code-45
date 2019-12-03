#!/usr/bin/python3
from csepy.System.Models.Context.ContextFactory import GetContext


def EnqueueAndRun(request):
    context = GetContext()
    context.CommandQueue.EnqueueCommands([request])
    context.CommandQueue.RunCommands()
