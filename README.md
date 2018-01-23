# PERSONAL TRAINNING TOOL #
기존 네이티브 안드로이드 버전을 웹버전으로 변경 


### Specification
* python3: v3.6.1
* django: v1.11.7
* bulma: 0.6.2
* vue: 2.5.1


### Node package ###
* gulp: ^3.9.1
* gulp-typescript: ^3.2.2 (현 버전에서는 사용하지 않음)
* tsify: ^3.0.3 (현 버전에서는 사용하지 않음)
* typescript: ^2.5.2 (현 버전에서는 사용하지 않음)


## Mac OSX
* npm install
```shell
$> npm install
```

* gulp를 이용하여 front-end파일을 프로젝트 배포 폴더로 이동
```shell
$> gulp
```

* brew를 이용한 python3 설치 및 virtualenv 설정
```shell
$> brew install python3
$> python3 -m venv venv/pttool
$> source venv/pttool/bin/activate
```

* django 설치 
```shell
$> pip install django==1.11.7
```

* run pttool application 
``` shell
$> cd pttool_web
$> python manage.py runserver 0:8000
```


* [http://127.0.0.1:8000](http://127.0.0.1:8000)