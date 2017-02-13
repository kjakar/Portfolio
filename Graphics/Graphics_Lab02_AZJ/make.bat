@set JAVAC="C:/Program Files/Java/jdk1.8.0_101/bin/javac.exe"
@set CLASS_PATH=".;lwjgl/jar/lwjgl.jar"
@set MAIN_SOURCE_FILE="Model3D.java"

@del /S *.class
%JAVAC% -cp %CLASS_PATH% %MAIN_SOURCE_FILE%