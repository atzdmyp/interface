import jenkins

# 脚本构建jenkins

jenkins_server_url = "http://localhost:8080"
user_id = "chennan"
api_token = "2e8babe0fd656fee163851f1833bf4a0"
job_name = "interfaceTest01"
params = {
    'params1': 'value1',
    'params2': 'value2'
}
build_number = 0
# 实例化Jenkins
server = jenkins.Jenkins(jenkins_server_url, user_id, api_token)
# 构建带参数的job
server.build_job(job_name)
# 获取job的相关信息
name = server.get_job_info(job_name)
# 获取job的最后次构建号
build_number = server.get_job_info(job_name)['lastBuild']['number']
# 获取job名为job_name的job的某次构建的执行结果状态
result = server.get_build_info(job_name, build_number)['result']
# 判断job名为job_name的job的某次构建是否还在构建中
status = server.get_build_info(job_name, build_number)['building']

print(build_number)
print(result)
print(status)

