Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> buildings = 3
... ninjas =  25
... samurai = 40
... tunnels = 2
... buildings * ninjas * samurai * tunnels
... 
SyntaxError: multiple statements found while compiling a single statement
>>> buildings = 3
>>> ninjas = 25
>>> samurai = 40
>>> tunnels = 2
>>> ninjas * buildings
75
>>> samurai * tunnels
80
