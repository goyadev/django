# Goya - She Codes News Project
## About This Project
This project was created as the Django project for She Codes Plus 2023/2024. 
## How To Run This Code
Django 4.2.2
1. Clone repo
2. Start venv
3. Migrate data with `python manage.py runserver`

## Database Schema
![ My ERD ](./images/ERD-shecodesnews.png)

## Project Features
- [x] Order stories by date
![ Screenshot of stories ordered by date ]( ./images/ordered-stories-date.png )
- [x] Styled "new story" form
![ Basic styling for form ]( ./images/styled-new-story-form.png )
- [x] Story images
![ Images from stories ]( ./images/ordered-stories-date.png )
- [x] Log-in/log-out
![ Log in ]( ./images/login.png )
![ Log out ]( ./images/logout.png)
- [x] "Account view" page
![ User profile page ]( ./images/account-view.png)
- [x] "Create Account" page
![ Basic styled create account page ]( ./images/create-account.png)
- [x] View stories by author
![ Author view in profile ]( ./images/stories-by-author.png )
- [x] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in
![ login visible, logged out user ]( ./images/login-visible.png)
![ logout visible, logged in user ]( ./images/logout-visible.png)
- [x] "Create Story" functionality only available when user is logged in
![ In nav, the create story function is not visible if not logged in ]( ./images/write-story-visible.png)

## Additional Features:
- [x] Add the ability to comment on stories within the story page
![ On page article comments immediately visible]( ./images/add-comment.png )
- [x] Gracefully handle the error where someone tries to create a new story when they are not logged in.
![ The create new story auto-redirects to login page if clicked while not logged in]( ./images/graceful-redirect-add-story.png)

## Future Ideas:
- [ ] Dark mode feature toggle
- [ ] Add the ability to update and delete stories 
- [ ] Add the ability for user to edit and delete account
- [ ] Add the ability to “favourite” stories and see a page with your favourite
- [ ] Category or keyword search function


