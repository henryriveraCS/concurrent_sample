using <code>pool.submit(func)</code> runs almost twice as fast the original script (using only with() statement). 
There's more room for improvement if the OS walking is split into different threads as well
but for now we just assume we want to optimize for concurrent file copying:
```
python3 co.py 
Time to execute script concurrently: 0.006451845169067383
Time to execute linear script: 0.011797904968261719
python3 co.py
Time to execute script concurrently: 0.0044879913330078125
Time to execute linear script: 0.005181789398193359
python3 co.py
Time to execute script concurrently: 0.006019115447998047
Time to execute linear script: 0.011581897735595703
python3 co.py
Time to execute script concurrently: 0.0054569244384765625
Time to execute linear script: 0.010963916778564453
python3 co.py
Time to execute script concurrently: 0.005223989486694336
Time to execute linear script: 0.0065729618072509766
python3 co.py
Time to execute script concurrently: 0.005241870880126953
Time to execute linear script: 0.0076122283935546875
```

You can run this script by git cloning it then just using <code>python3 co.py</code>
