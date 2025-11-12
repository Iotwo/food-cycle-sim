# Model field pattern data syntax and description

Field is builded with patterns. Patterns are just text matrix. Every position in matrix is a single symbol mapping to an existing Ground class or subclass. Each class has it's effects for unit exemplar occupying it. Modifyers are: speed, 

## Types

* Ground - basic class with no modifyers.

1. Fertility affecting types
   - Rock has greater fertility value than Ground
   - Grass has lesser fertility value than Ground

2. Illumination affecting types
   - Dirt has lesser illumination value than Ground
   - Water has greater illumination value than Ground

3. Speed affecting types
   - Sand has negative speed effect
   - Ice has positive speed effect

## Ground types symbols

* 'G' - basic ground class
* 'D' - dirt class
* 'i' - ice class
* '>' - rock class
* 'V' - grass class
* 'w' - water class
* ':' - sand class
