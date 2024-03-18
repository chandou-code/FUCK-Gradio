@echo off
java --add-opens java.base/java.lang=ALL-UNNAMED -jar browsermob-dist-2.1.4.jar --use-littleproxy false
pause
