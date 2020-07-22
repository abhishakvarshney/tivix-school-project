# tivix-school-project

- Run the command `docker-compose build`
- Now run the command `docker-compose up`
- open [phpMyAdmin](http://localhost:8070) or by copy-paste-hit on browser http://localhost:8070
- Username: platform_admin  
Password: pb_dev_env
- Import **platform_school.sql** and dump it on platform_school database.
- Get Postman collection of all the APIs from here: [Link](https://www.getpostman.com/collections/43f24a61a397b0f4a068)

### Support:
- If there is anything which bother you in this project feel free to contact me.

### Thoughts:
- Tried to follow the coding best practices like AES-256 encryption of personal information like firstname, lastname, password etc.
- Applied Request Validator. Thanks to Voluptuous a JavaScript JOI like library to provide request validation.
- Custom logging is implemented in django project setting.
- Nginx is already configured so you don't have tp worry about that.
- For deletion of account soft-delete is used.
- Minimum size based external docker-images are used.

### Future Prospects
  - sessionId based session may be implemented that's why didn't handle authorization on update and delete.