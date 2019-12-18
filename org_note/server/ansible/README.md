# 用Ansible playbook 部屬到test server 
```
ansible-playbook game_server.yaml --limit niu1
```
# 用Ansible playbook 部屬report server
```
ansible-playbook  --extra-vars '@testbed_passwd.yml' dpy_report.yaml  --limit niu1 --vault-password-file ./testbed_secret.txt 
```