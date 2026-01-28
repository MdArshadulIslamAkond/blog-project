Functional Requirements
1. User Authentication

●User Registration (Sign Up)

●User Login & Logout

●Only authenticated users can create blog posts

2. Blog Post Management (CRUD)

Authenticated users must be able to: - Create a new blog post - View all blog posts - View single blog post

details - Update their own blog posts - Delete their own blog posts

Each blog post must contain: - Title - Content - Author - Created Date - Updated Date (optional)

3. Blog Listing & Details

●Home page should display a list of all blog posts

●Each post should have a details page

●Blog posts should display author name and publish date

4. Authorization Rules

●A user can edit or delete only their own posts

●Other users’ posts should be read-only

5. UI Requirements

●Use Django Templates

●Clean and simple UI

●Navigation bar with Login, Logout, Register links
