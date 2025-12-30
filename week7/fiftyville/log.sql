-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports
WHERE year = 2024 AND month = 7 AND day = 28 AND street = "Humphrey Street";

--theft of cs50 duck took place at 10:15am at Humphrey Street bakery.
SELECT transcript FROM interviews
WHERE year = 2024 AND month = 7 AND day = 28 AND transcript LIKE "%bakery%";

--first transcript:
--Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs
WHERE year = 2024 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit");
--Name of the suspects: vanessa, barry, iman, sofia, luca, diana, kelsey, bruce.

--second transcript:
--I don't know the thief's name, but it was someone I recognized.
--Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
SELECT name FROM people
WHERE id IN (SELECT person_id FROM bank_accounts
WHERE account_number IN (SELECT account_number FROM atm_transactions
WHERE year = 2024 AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));
--Name of the suspects: kenny, iman, benista, taylor, brooke, luca, diana, bruce.

--third transcript:
--As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--The thief then asked the person on the other end of the phone to purchase the flight ticket.
SELECT name FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = (SELECT id FROM flights WHERE year = 2024 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville") ORDER BY hour,minute LIMIT 1);
--Name of the suspects: Doris, sofia, bruce, edward, kelsay, taylor, kenny, luca.

--common suspects: luca, bruce

--phone call:
SELECT name FROM people
JOIN phone_calls ON phone_calls.caller == people.phone_number
WHERE year = 2024 AND month = 7 AND day = 28 AND duration < 60;

--suspect: Bruce

--ESCAPED TO:
SELECT city FROM airports
WHERE id = (SELECT destination_airport_id FROM flights WHERE year = 2024 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = "Fiftyville") ORDER BY hour, minute LIMIT 1);

--The city is New York

--Accomplice
SELECT phone_number FROM people WHERE name = "Bruce";
--phone number: (367) 555-5533
SELECT name FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE year = 2024 AND month = 7 AND day = 28 AND duration < 60 AND caller = "(367) 555-5533");
--suspect: Robin
