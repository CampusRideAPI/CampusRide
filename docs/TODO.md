# CampusRide - Minimal MVP TODO List

## Core Features (MVP Only)

### Ride Management

- [ ] Create new rides

  - [ ] Basic form for adding ride
  - [ ] Validation for required fields

- [ ] List all rides

  - [ ] Simple table/list display
  - [ ] Show ride details

- [ ] Delete rides
  - [ ] Basic delete functionality

## Database Model (SQLite)

### Ride Model

- [ ] Fields:
  - [ ] id (Primary Key)
  - [ ] departure_location (String)
  - [ ] arrival_location (String)
  - [ ] departure_time (DateTime)
  - [ ] available_seats (Integer)
  - [ ] driver_name (String)

## API Endpoints (FastAPI)

### Required for Full Points

- [ ] GET /rides
  - List all rides
- [ ] GET /rides/{id}
  - Get single ride details
- [ ] POST /rides
  - Create new ride
- [ ] PUT /rides/{id}
  - Update ride details (required for assessment points)
  - Update available seats
  - Update departure time
  - Update locations
- [ ] DELETE /rides/{id}
  - Remove ride

### Endpoint Details for Points Checklist

- [ ] Implement all HTTP verbs (2 points)
  - GET ✓
  - POST ✓
  - PUT ✓
  - DELETE ✓
- [ ] Follow REST API best practices (2 points)
  - Proper status codes
  - Consistent endpoint naming
  - Clear request/response structure
- [ ] Request validation (2 points)
  - Validate input data types
  - Validate required fields
- [ ] Response validation (2 points)
  - Consistent response format
  - Proper error responses

## Frontend (Flask + HTML)

### Pages

- [ ] Home page

  - [ ] Simple HTML table of rides
  - [ ] Link to create new ride

- [ ] Create ride page

  - [ ] Basic HTML form
  - [ ] Submit button

- [ ] Update ride page
  - [ ] Basic update form
  - [ ] Submit changes button

## Optional Features

- [ ] Basic sorting by date
- [ ] Basic form validation messages
- [ ] Confirmation for delete
- [ ] Simple navigation between pages

## Documentation

- [ ] Setup instructions
- [ ] API endpoints list

## Definition of Done:

1. User can create a new ride
2. User can view all rides
3. User can update a ride
4. User can delete a ride
5. Data is stored in SQLite
6. Basic functionality works

Keep in mind:

- No styling needed
- Just basic HTML
- Focus on functionality over appearance
- Keep it as simple as possible
- Implement all required HTTP verbs for points
