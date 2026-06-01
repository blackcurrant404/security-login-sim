Idea is to do a simple login simulator that can be used to test other applications like "brute force simulator" or "log-analyzer"

# security login simulator plan

## V1
- program handles single login attempt per run 
- compares given password to the hardcoded one
- print result ("accepted" or "failed")   
- saves the attempt on log file (input ip/default + result)

## V2
- change the verify function result to boolean value instead of string
- timestamps for login attempts in the log file
- support for multiple users, istead of only root

## V3 
- change the login system into HTTP-based mini server
- handle authentication via HTTP requests (/login endpoin)
- move authentication logic into separate service layer
- server returns JSON responses (success / failure)
- server handles logging of all authentication attempts

## V4
- HTML frontend
- home page (/)
- login UI route
- backend and frontend integration
