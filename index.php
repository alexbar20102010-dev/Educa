<?php
// Путь к исполняемому файлу Python и Django
$python_path = '/usr/local/bin/python3.11';
$project_path = dirname(__FILE__);
$manage_path = $project_path . '/manage.py';

// Команда для запуска Django
$command = escapeshellcmd($python_path . ' ' . $manage_path . ' runserver');

// Вывод для отладки (удалите в продакшене)
echo "<!-- Project path: " . $project_path . " -->\n";
echo "<!-- Python path: " . $python_path . " -->\n";

// Запускаем Django
$output = shell_exec($command . ' 2>&1');
echo $output;
?>