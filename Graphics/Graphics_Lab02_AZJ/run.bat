@set JAVA="C:/Program Files/Java/jdk1.8.0_101/bin/java.exe"
@set CLASS_PATH=".;lwjgl/jar/lwjgl.jar"
@set NATIVE_PATH="lwjgl/native/"
@set MAIN_CLASS="Model3D"

%JAVA% -cp %CLASS_PATH% -Djava.library.path=%NATIVE_PATH% %MAIN_CLASS%