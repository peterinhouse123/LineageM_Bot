@echo off
%1 -s %2 shell sendevent /dev/input/event5 3 57 6

%1 -s %2 shell sendevent /dev/input/event5 3 57 6

     
%1 -s %2 shell sendevent /dev/input/event5 1 330 1

     
%1 -s %2 shell sendevent /dev/input/event5 3 53 %3

     
%1 -s %2 shell sendevent /dev/input/event5 3 54 %4

     
%1 -s %2 shell sendevent /dev/input/event5 0 0 0


     
%1 -s %2 shell sendevent /dev/input/event5 3 53 %5

     
%1 -s %2 shell sendevent /dev/input/event5 3 54 %6

     
%1 -s %2 shell sendevent /dev/input/event5 0 0 0

ping 127.0.0.1 -n %9 -w 1000 > nul

     
%1 -s %2 shell sendevent /dev/input/event5 3 53 %7

     
%1 -s %2 shell sendevent /dev/input/event5 3 54 %8

     
%1 -s %2 shell sendevent /dev/input/event5 0 0 0

%1 -s %2 shell sendevent /dev/input/event5 3 57 4294967295

     
%1 -s %2 shell sendevent /dev/input/event5 1 330 0

     
%1 -s %2 shell sendevent /dev/input/event5 0 0 0
