# Qwizyo Api

## Description

The Quiz Making App is a web application designed to allow tutors to create quizzes for students. Users can register an account, create quizzes with multiple-choice questions, or other type and students take quizzes created by tutors, and view their quiz results.

## Endpoints

### Authentication Endpoints

- **POST /api/auth/register:**
  - Register a new user (tutor or student).

- **POST /api/auth/login:**
  - Authenticate user credentials and generate an access token.

### User Management Endpoints

- **GET /api/users/me:**
  - Retrieve the current user's profile information.

- **PUT /api/users/me:**
  - Update the current user's profile information.

- **GET /api/users/{user_id}:**
  - Retrieve the profile information of a specific user (for admins or tutors).

### Group Management Endpoints

- **GET /api/groups:**
  - Retrieve a list of groups associated with the current user (tutor).

- **POST /api/groups:**
  - Create a new group.

- **GET /api/groups/{group_id}:**
  - Retrieve details of a specific group.

- **PUT /api/groups/{group_id}:**
  - Update group details.

- **DELETE /api/groups/{group_id}:**
  - Delete a group.

### Quiz Management Endpoints

- **GET /api/quizzes:**
  - Retrieve a list of quizzes created by the current user (tutor).

- **POST /api/quizzes:**
  - Create a new quiz.

- **GET /api/quizzes/{quiz_id}:**
  - Retrieve details of a specific quiz.

- **PUT /api/quizzes/{quiz_id}:**
  - Update quiz details.

- **DELETE /api/quizzes/{quiz_id}:**
  - Delete a quiz.

### Quiz Assignment Endpoints

- **POST /api/assignments:**
  - Assign a quiz to a group or individual student.

- **GET /api/assignments:**
  - Retrieve student assignments

- **GET /api/assignments/{assignment_id}:**
  - Retrieve details of a specific assignment.

- **PUT /api/assignments/{assignment_id}:**
  - Update assignment details.

- **DELETE /api/assignments/{assignment_id}:**
  - Delete an assignment.

- **GET /api/groups/{group_id}/assignments:**
  - Retrieve group assignments

- **GET /api/quizzes/{quiz_id}/assignments:**
  - Retrieve quiz assignments

### Quiz Submission Endpoints

- **POST /api/submissions:**
  - Submit answers for a quiz. (student)

- **GET /api/submissions:**
  - Retrieve student submissions. (student)

- **GET /api/assignments/{assignment_id}/submissions:**
  - Retrieve assignment submissions. (tutor)

- **GET /api/quizzes/{quiz_id}/submissions:**
  - Retrieve assignment submissions. (tutor)

- **GET /api/submissions/{submission_id}:**
  - Retrieve details of a specific submission.

- **PUT /api/submissions/{submission_id}:**
  - Update submission details (e.g., resubmit answers). (tutor)

- **DELETE /api/submissions/{submission_id}:**
  - Delete a submission. (tutor)

### Miscellaneous Endpoints

- **GET /api/ping:**
  - Check if the server is up and running (for health checks).

- **GET /api/docs:**
  - Access API documentation (e.g., Swagger UI).
