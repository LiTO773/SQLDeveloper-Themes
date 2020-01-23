## What is this folder for?
This folder contains all the scripts used for converting schemes/themes to the 
SQL Developer format. Feel free to use whatever programming language you believe
it's best for the job.

## Color guide
SQLDeveloper stores color values in decimal. In order to get the corresponding 
color value from hexadecimal, it needs to be inverted, then converted to 
decimal and finally subtracted 1. To get a better grasp on how this is done
take a look at the examples below:

Examples:

| Color | Hexadecimal | Decimal  | SQLDeveloper Operation  | Result        |
|-------|-------------|----------|-------------------------|---------------|
| Black | #000000     | 0        | 0 - 16777215 - 1        | **-16777216** |
| White | #FFFFFF     | 16777215 | 16777215 - 16777215 - 1 | **-1**        |
| Cyan  | #00FFFF     | 65535    | 65535 - 16777215 - 1    | **-16711681** |
