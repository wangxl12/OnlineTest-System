## Switch to: [GithubPage](https://wangxl12.github.io/OnlineTest-System/)
# OnlineTest-System
<font face="楷体" size=4>使用Django开发简单的在线习题测试系统，系统角色为学生和教师，习题类型有单选题、多选题、填空题，教师可在线录入或以文件方式上传试题。系统还扩展签到、在线搜题、数据统计等功能（不完善，有未解决的Bug），由于时间关系无法进一步将上述功能进行完善，但是预留了功能扩展接口，便于开发人员根据自己的需要进行功能的优化。</font>

# 依赖库的安装、迁移数据库、启动、登录教师用户、创建教师用户：

<font face="楷体" size=4>为了方便操作，将相关指令集成于两个文件中，即：</font>

`./RUNME/runserver.bat`

<font face="楷体" size=4>与</font>

`./RUNME/createSuperuser.bat`

<font face="楷体" size=4>操作方法：</font>

<font face="楷体" size=4>下载本项目文件置本地，找到`OnlineTest-System/RUNME/runserver.bat`。</font>

<font face="楷体" size=4>如果你没有python虚拟环境，并且想直接将本项目所需的相关依赖库安装于基环境，直接双击`runserver.bat`即可，系统将自动执行依赖库的安装、数据库迁移与启动指令，**.bat文件可以多次运行，不会带来负面影响**；如果你想创建教师用户，在`RUNME`目录下打开命令行，输入`createSuperuser.bat`即可，注意，与`runserver.bat`不同的是，双击该文件无效。</font>

<font face="楷体" size=4>如果你想在自己的虚拟环境中运行，首先需要切换到自己的虚拟环境中，然后切换到`RUNME`目录下，输入两个`.bat`文件的文件名即可。</font>

<font face="楷体" size=4>**如果你想自己输入指令来执行，请继续参照下文：**</font>

## 依赖库安装：

```shell
cd OnlineTest-System
pip install -r requirement.txt
```

## 迁移数据库：

```shell
python manage.py makemigrations
python manage.py migrate
```

## 启动：

```shell
python manage.py runserver 80
```

## 登陆教师界面：

```shell
访问 /admin
```

## 创建教师账户：

```shell
py manage.py createsuperuser
```

## 部分功能界面展示

### 登录界面：

![登录界面](./imgs/登录界面.png#pic_center)

## 学生界面：

![学生界面](./imgs/学生界面.png#pic_center)

## 修改密码界面：

![登录界面](./imgs/修改密码界面.png#pic_center)

## 答卷界面：

![答卷界面](./imgs/答卷界面.png#pic_center)

<font face="楷体" color=red size=4>Hints: 如果该界面不能上下滑动，可以通过点击右侧的题目编号来定位题目。</font>

## 教师界面：

![教师登录界面](./imgs/教师登录界面.png#pic_center)

![教师功能界面](./imgs/教师功能界面.png#pic_center)

![发布试卷界面](./imgs/发布试卷界面.png#pic_center)

![添加签到界面](./imgs/添加签到界面.png#pic_center)

## 数据可视化（数据可视化只是展示了随机数，并未展示真正的测试数据，这一功能有待扩展）：

![数据可视化界面](./imgs/数据可视化1.png#pic_center)

![数据可视化界面](./imgs/数据可视化2.png#pic_center)

![数据可视化界面](./imgs/数据可视化3.png#pic_center)

# 为了帮助理解，下面附部分文件功能介绍

- 核心功能文件为onlinetest、static、testsystem三个文件夹。
- static为静态文件，提供美化界面的功能。
- onlinetest设置重要的配置参数。
- testsystem下核心为templates文件夹+若干个.py文件
  - templates文件夹下为html文件（设计界面）。
  - .py文件设计后端功能：models.py创建数据库、数据表；views.py处理核心功能...
