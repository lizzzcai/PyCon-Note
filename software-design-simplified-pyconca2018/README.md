# Software Design Simplified



# Value Objects & Service Objects

## Value Objects

* Just data, no behaviour
* Useful for validation, building comparators
* Simplifies service interfaces
* Should `NOT` be ORM objects
* Could be dictionaries, but probably shouldn't be

## Service Objects

* A collection of stateless methods for operating on your data.
* Seperation of concerns centers around determining how much a method should do.

# Naming Alert

## Separation of Concerns

Domain
* FetchEmailContent
* GenerateHTMLEmail
* SendHTMLEmail

System
* I/O

⋅⋅* Database
⋅⋅* Filesystem
⋅⋅* Network

* Logic
* Coordination
* Workflow

## Use Layers to Create System Separation of Concerns