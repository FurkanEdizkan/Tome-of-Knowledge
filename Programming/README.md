# Learning Tasks

I do beliave learning by doing, so in order to convince myself I have basic knowledge on a programming language I have created following learning projects.

## Table of Contents
- [Learning Tasks](#learning-tasks)
  - [Table of Contents](#table-of-contents)
  - [Microservice + Database + Communication Layer (REST/gRPC Switchable)](#microservice--database--communication-layer-restgrpc-switchable)
    - [Description](#description)
    - [Requirements](#requirements)
    - [Skills Covered](#skills-covered)
  - [Local App with UI + Authentication + Encryption + Local DB](#local-app-with-ui--authentication--encryption--local-db)
    - [Description](#description-1)
    - [App Functionality](#app-functionality)
    - [Skills Covered](#skills-covered-1)
  - [Software Automation System (Pipeline + Build + Scheduling)](#software-automation-system-pipeline--build--scheduling)
    - [Description](#description-2)
    - [Features](#features)
    - [Skills Covered](#skills-covered-2)

---

## Microservice + Database + Communication Layer (REST/gRPC Switchable)

Learn backend fundamentals, networking, serialization, data persistence, testing microservice boundaries.

### Description

Build a small microservice that can operate in two modes:

* **REST Mode** (JSON over HTTP)
* **gRPC Mode** (Protocol Buffers)

The service manages a simple entity (choose one):

* `Task`
* `User`
* `SensorData`
* `Product`

### Requirements

1. **Local Database**

   * SQLite (perfect for offline, portable learning)
   * Optional: PostgreSQL in Docker if you want real DB practice

2. **Data Model**

   * `id`
   * `name`
   * `created_at`
   * `updated_at`

3. **Endpoints/RPCs**

   * Create
   * Get by ID
   * List
   * Update
   * Delete

4. **Communication Layer Switching**

   * Start the service in either REST or gRPC mode using a CLI flag:

     ```
     ./service --mode=rest  
     ./service --mode=grpc
     ```

5. **Optional**

   * Add pagination
   * Add metrics endpoint (`/metrics`)
   * Add logging middleware
   * Add unit tests + integration tests

### Skills Covered

* DB schema design
* CRUD logic
* REST & gRPC
* Serialization (JSON, Protobuf)
* Testing web services
* CLI arguments
* Microservice architecture basics

---

## Local App with UI + Authentication + Encryption + Local DB

Learn about UI, secure services, authentication, encryption, and user management.

### Description

Create a simple local desktop app or CLI tool (choose depending on language):

* CLI app
* Desktop app

### App Functionality

**User-facing app with login and secure storage:**

1. **Signup/Login System**

   * Store hashed passwords (bcrypt, argon2, PBKDF2)
   * Login form or CLI input

2. **Local Encrypted Database**

   * SQLite
   * Optionally encrypt whole DB using:

     * SQLCipher
     * custom AES encryption for sensitive fields

3. **User Interface**

   * Show a small dashboard after login
   * CRUD for user’s personal notes or settings
   * Light/Dark mode profile stored in DB

4. **Security**

   * Input validation
   * Hashing
   * JWT or session tokens (even locally)
   * No plain-text passwords ever

5. **Optional**

   * Implement “remember me” using encrypted tokens
   * Add biometric mock authentication (PIN or challenge)
   * Add role-based access (admin/user)

### Skills Covered

* UI building
* Authentication flow
* Encryption and password hashing
* Database queries
* Session/token management
* App architecture

---

## Software Automation System (Pipeline + Build + Scheduling)

**Goal:** Learn DevOps basics, tooling, orchestration, automation, background processing.

### Description

Build a small **automation orchestrator** that can:

1. **Run tasks automatically on schedule**
2. **Trigger builds or scripts**
3. **Log results**
4. **Send notifications (local logs or file system)**

### Features

1. **Task Runner**

   * YAML/JSON config describing tasks
   * Example:

     ```yaml
     tasks:
       - name: compile_code
         command: "make"
         schedule: "every 5 minutes"
       - name: backup_db
         command: "./backup.sh"
         schedule: "daily"
     ```

2. **Scheduler**

   * Cron-like system
   * Or simple interval timers

3. **Logging System**

   * Save logs to file
   * Keep history (max 100 logs)

4. **Plugins or Modules**

   * Add new automation tasks easily
   * Example: Notify by writing to a local file or sending desktop notification

5. **Optional**

   * REST API to show what tasks are running
   * A dashboard UI
   * Add Docker support to run tasks inside containers

### Skills Covered

* Automation scripting
* Task scheduling
* Logging & monitoring
* Parsing configs
* Building extensible systems
* Understanding build pipeline concepts
* DevOps mindset

---
