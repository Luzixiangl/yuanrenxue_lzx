# 边抠代码边运行查看缺什么时，出现卡死？
# 即进入到了蜜罐里去了，出现该情况只有两种可能：
# 1、浏览器指纹：复制代码在浏览器下尝试运行，如正常即为浏览器指纹引起
# 2、格式化检测：在确认是格式化检测引起：复制代码且在代码第一行增加debugger;然后F11逐个函数排查找出格式化检测代码（即代码进入死循环里头）并删除之