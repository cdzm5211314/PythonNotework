### Ubuntu 16.04 服务器:
### VMware Workstation快捷键使用:
- 释放鼠标光标: ctrl + alt 释放鼠标光标
- 全屏/退出全屏(切换): ctrl + alt + enter 
- 退出终端: exit 或 ctrl + d
- 清屏: clear 或 ctrl + L


### SSH链接另一台服务器:  ssh 用户名@IP地址

### SSH文件(或目录)的上传与下载[服务器]:
- 从服务器上下载文件(目录)
> scp username@servername:/path/filename /var/www/local_dir（本地目录）  
> scp -r username@servername:/var/www/remote_dir/（远程目录） /var/www/local_dir（本地目录）  
- 上传本地文件(或目录)到服务器
> scp /path/filename username@servername:/path  
> scp -r local_dir username@servername:remote_dir  

- 安装: sudo apt-get install lrzsz
> 本地文件上传到服务器: rz  
> 服务器文件下载到本地: sz test.tar  


*************************************************************************************************************
### Linux基本命令使用大全:
- 关机: halt 或 shutdown -h now(立刻关机) 或 shutdown -h 10(10分钟后自动关机) 或 shutdown -h 14:30(时间为14:30关机,shutdown -c取消关机)
- 重启: reboot 或 shutdown -r now(立刻重启) 或 shutdown -r 10(10分钟后自动重启) 或 shutdown -r 20:35(时间为20:35重启,shutdown -c取消重启)
- 退出终端: exit 或 ctrl + d
- 清屏: clear 或 ctrl + L
- 查看当前目录: pwd
- 进入目录: cd path 或 cd /(根目录) cd ~(用户目录)
- 查看当前目录下的所有文件与目录: ls 或 ls -l 或 ls -a 或 tree  /opt
- 目录操作: 
    - 创建一层或多层目录: mkdir dir 或 mkdir -p /dir1/dir2/dir3/dir4
    - 拷贝目录: cp -r /opt/learn /opt/learn2
    - 重命名目录: mv /opt/learn2 /opt/learn3   
    - 删除与强制删除目录: rmdir dir 或 rm -rf /opt/learn3
- 文件操作: 
    - 创建文件: vi file 或 touch file 或 cat > /opt/learn/catfile
    - 拷贝或剪切文件: cp hello.txt /opt/test 或 mv hello.txt /opt/test
    - 重命名文件: mv file1 file2
    - 删除与强制删除文件: rm /opt/test/hello.cp 或 rm -f /opt/test/hello.mv
- 文件查看操作:
    - 屏幕上输出文本内容: cat file
    - 分屏输出文本内容: more file
    - 分屏输出文本内容并按需加载文件(适用于大文件的查看): less file
    - 只输出文件的头10行: head -n 10 file
    - 只输出文件的尾20行: tail -n 20 file    
- 文件编辑操作: vi file 或 vim file 
    - 在命令行模式下,用于给文件显示行号: :set number
    - 从命令模式进入编辑模式: i(插入文本) 或者 a(追加文本)
    - 从编辑模式进入命令模式: Esc
    - 保存并退出或存盘退出: :wq 或 ZZ
    - 退出或强制退出: :q 或 :q!
    - 在光标所在行的上方添加一行: O
    - 在光标所在行的下方添加一行: o
    - 删除一行: dd
    - 删除一个字符: x
    - 光标移至文本第n行: :n
    - 光标移动到文本的行首或行尾: ^ 或 $ 
    - 光标移动到文本的首行或末尾: gg 或 G
    - 查找某个字符串: / ---> n(继续查找)
- 文件权限操作: chmod [权限] [文件或目录]
    - 左边10位中的第一位代表文件类型,d ---> 代表目录, -  ---> 代表普通文件, l  ---> 代表链接文件  
    - 左边10位中的后9位代表权限,前3位代表文件所有者的权限(用u表示),中间3位代表文件所在组的权限(用g表示),后3位代表其他组的权限(用o表示)  
    - 权限rwx的意义: 权限 r 或数字 4 ---> 表示可读, 权限 w 或数字 2 ---> 表示可写, 权限 x 或数字 1 ---> 表示可执行  
    - chmod u+r hello.txt ---> 为hello.txt文件所有者添加可读权限
    - chmod g+w hello.txt ---> 为hello.txt文件所在组添加可写权限
    - chmod o+x hello.txt ---> 为hello.txt文件其他组添加可执行权限
    - chmod a+w hello.txt ---> 为所有三种角色添加可写权限
    - chmod 777 hello.txt ---> 将hello.txt的权限设为rwxrwxrwx
    - chmod 645 hello.txt ---> 将hello.txt的权限设为rw-r--r-x
- 解压缩文件:         
    - tar -cvf hello.tar hello.txt      将hello.txt归档并命名成hello.tar
    - tar -xvf hello.tar                解压缩hello.tar
    - tar -zcvf hello.tar.gz hello.txt  将hello.txt归档并压缩成hello.tar.gz
    - tar -zxvf hello.tar.gz            解压缩hello.tar.gz
    - gzip hello.tar                    将归档文件hello.tar压缩成hello.tar.gz
    - gzip -d hello.tar.gz              解压缩文件成hello.tar
    - zip hello.zip hello.txt           将hello.txt压缩并命名成hello.zip
    - unzip hello.zip                   解压缩hello.zip





