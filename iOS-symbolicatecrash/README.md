
# ReSymbol

Auto recursive iOS Symbol in Crash Logs. iOS奔溃日志自动解析(符号化).

## Usage

`YourAppName.app` 获取方法, 在` Xcode` 的 `Organizer` -> `Archives`中选中你的 app -> 右键 `Show in Finder`
以下前两个文件都在此目录下.

把以下文件放在同一个目录下:

* YourAppName.app
* YourAppName.app.dSYM
* CrashFile.crash

参数说明:
* `-c` 崩溃日志文件 -> `CrashFile.crash` 文件则输入 `CrashFile`
* `-a` APP文件 -> `YourAppName.app` 输入 `YourAppName`

```python
python ReSymbol.py -c "CrashFileName" -a "YourAppName" 
```
如果出现:

输入:

`export DEVELOPER_DIR="/Applications/XCode.app/Contents/Developer"`

## Sample

目录下有文件:
* 30-1.crash
* BPCoachClient.app
* BPCoachClient.app.dSYM

执行命令: `python ReSymbol.py -c "30-1" -a "BPCoachClient"`

```python
GrayLands-MacPro-Compony:1 grayland$ python ReSymbol.py -c "30-1" -a "BPCoachClient"
['ReSymbol.py', '-c', '30-1', '-a', 'BPCoachClient']
fileName= 30-1
version= 
appName= BPCoachClient
正在解析...
## Warning: Unable to symbolicate from required binary: /Users/languilin/Library/Developer/Xcode/iOS DeviceSupport/10.3.3 (14G60)/Symbols/System/Library/Frameworks/CoreMotion.framework/CoreMotion
解析完成!!!
```

生成文件 `30-1.log`:

``` Before
Application Specific Information:
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: 'Application tried to present modally an active controller <BPSportPlanReportWithLogVC: 0x114159000>.'

Thread 0 Crashed:
0   CoreFoundation                  0x000000018e876fe0 0x18e74a000 + 1232864 (<redacted> + 124)
1   libobjc.A.dylib                 0x000000018d2d8538 0x18d2d0000 + 34104 (objc_exception_throw + 56)
2   UIKit                           0x0000000194d19ebc 0x194999000 + 3673788 (<redacted> + 4800)
3   UIKit                           0x0000000194aa2588 0x194999000 + 1086856 (<redacted> + 268)
4   UIKit                           0x0000000194ace79c 0x194999000 + 1267612 (<redacted> + 148)
5   UIKit                           0x0000000194acd5a0 0x194999000 + 1263008 (<redacted> + 132)
6   UIKit                           0x0000000194c1bb28 0x194999000 + 2632488 (<redacted> + 724)
7   UIKit                           0x00000001949e1538 0x194999000 + 296248 (<redacted> + 492)
8   UIKit                           0x00000001949e1060 0x194999000 + 295008 (<redacted> + 312)
9   UIKit                           0x00000001949e0e7c 0x194999000 + 294524 (<redacted> + 160)
10  QuartzCore                      0x0000000191b920d4 0x191a7f000 + 1126612 (<redacted> + 260)
11  libdispatch.dylib               0x000000018d72e9a0 0x18d72d000 + 6560 (<redacted> + 16)
12  libdispatch.dylib               0x000000018d7335e8 0x18d72d000 + 26088 (_dispatch_main_queue_callback_4CF + 996)
13  CoreFoundation                  0x000000018e8250c8 0x18e74a000 + 897224 (<redacted> + 12)
14  CoreFoundation                  0x000000018e822ce4 0x18e74a000 + 888036 (<redacted> + 1572)
15  CoreFoundation                  0x000000018e752da4 0x18e74a000 + 36260 (CFRunLoopRunSpecific + 424)
16  GraphicsServices                0x00000001901bd074 0x1901b1000 + 49268 (GSEventRunModal + 100)
17  UIKit                           0x0000000194a0dc9c 0x194999000 + 478364 (UIApplicationMain + 208)
18  BPCoachClient                   0x0000000100221b50 0x1000d8000 + 1350480 (main + 124)
19  libdyld.dylib                   0x000000018d76159c 0x18d75d000 + 17820 (<redacted> + 4)

Thread 1:
0   libsystem_kernel.dylib          0x000000018d871a88 0x18d852000 + 129672 (__workq_kernreturn + 8)
1   libsystem_pthread.dylib         0x000000018d9371a4 0x18d936000 + 4516 (_pthread_wqthread + 1260)

```

```After
Application Specific Information:
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: 'Application tried to present modally an active controller <BPSportPlanReportWithLogVC: 0x114159000>.'

Thread 0 Crashed:
0   CoreFoundation                  0x000000018e876fe0 __exceptionPreprocess + 124
1   libobjc.A.dylib                 0x000000018d2d8538 objc_exception_throw + 56
2   UIKit                           0x0000000194d19ebc -[UIViewController _presentViewController:withAnimationController:completion:] + 4800
3   UIKit                           0x0000000194aa2588 -[_UIViewControllerTransitionCoordinator _applyBlocks:releaseBlocks:] + 268
4   UIKit                           0x0000000194ace79c -[_UIViewControllerTransitionContext _runAlongsideCompletions] + 148
5   UIKit                           0x0000000194acd5a0 -[_UIViewControllerTransitionContext completeTransition:] + 132
6   UIKit                           0x0000000194c1bb28 __53-[_UINavigationParallaxTransition animateTransition:]_block_invoke.99 + 724
7   UIKit                           0x00000001949e1538 -[UIViewAnimationBlockDelegate _didEndBlockAnimation:finished:context:] + 492
8   UIKit                           0x00000001949e1060 -[UIViewAnimationState sendDelegateAnimationDidStop:finished:] + 312
9   UIKit                           0x00000001949e0e7c -[UIViewAnimationState animationDidStop:finished:] + 160
10  QuartzCore                      0x0000000191b920d4 CA::Layer::run_animation_callbacks+ 1126612 (void*) + 260
11  libdispatch.dylib               0x000000018d72e9a0 _dispatch_client_callout + 16
12  libdispatch.dylib               0x000000018d7335e8 _dispatch_main_queue_callback_4CF + 996
13  CoreFoundation                  0x000000018e8250c8 __CFRUNLOOP_IS_SERVICING_THE_MAIN_DISPATCH_QUEUE__ + 12
14  CoreFoundation                  0x000000018e822ce4 __CFRunLoopRun + 1572
15  CoreFoundation                  0x000000018e752da4 CFRunLoopRunSpecific + 424
16  GraphicsServices                0x00000001901bd074 GSEventRunModal + 100
17  UIKit                           0x0000000194a0dc9c UIApplicationMain + 208
18  BPCoachClient                   0x0000000100221b50 0x1000d8000 + 1350480 (main + 124)
19  libdyld.dylib                   0x000000018d76159c start + 4
```

