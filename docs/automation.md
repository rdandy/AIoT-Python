# Automation

Upload to Raspberry Pi 4B and run python file

## Actions on save

Tools > Actions on Save > Upload to default server

![0_actions_on_save.png](images/0_actions_on_save.png "0_actions_on_save.png")

## Add remote server

![1_deployment.png](images/1_deployment.png "1_deployment.png")

## run/debug configuration

Add remote run

![2_run_debug.png](images/2_run_debug.png "2_run_debug.png")

### Add **Before launch**

- Add Run File Watchers
- Add 

- ![3_run_configuration.png](images/3_run_configuration.png "3_run_configuration.png")

### external tool

![4_external_tool.png](images/4_external_tool.png "4_external_tool.png")

![5_external_tool_list.png](images/5_external_tool_list.png "5_external_tool_list.png")

![6_external_tool_runatraspberrypi.png](images/6_external_tool_runatraspberrypi.png "6_external_tool_runatraspberrypi.png")

### Tool Settings

program: python

Arguments: $RemoteProjectFileDir$/$FilePathRelativeToProjectRoot$

Working directory: $RemoteProjectFileDir$
