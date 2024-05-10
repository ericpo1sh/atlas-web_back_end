## Resources

**Read or watch:**

- [What Is PII, non-PII, and Personal Data?](https://intranet.atlasschool.com/rltoken/foPGuA-2Dz3K1Y40Zc_Qvg)
- [logging documentation](https://intranet.atlasschool.com/rltoken/U2Y7GJNwzVPTTvmpsyZ4sg)
- [bcrypt package](https://intranet.atlasschool.com/rltoken/rvDYLUTaAWqtkhSQAJf4zA)
- [Logging to Files, Setting Levels, and Formatting](https://intranet.atlasschool.com/rltoken/sxnkG_PQ8BcYeFGWAIRnjg)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/ZPysAXKK27_KivWx2yY8FA), **without the help of Google**:

- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

## What is personally identifiable information (PII)?

PII is often referenced by US government agencies and 
non-governmental organizations. Yet the US lacks one overriding law 
about PII, so your understanding of PII may differ depending on your 
particular situation.

## What pieces of information are considered PII?

According to NIST, PII can be divided into two categories: linked and linkable information.

**Linked information** is more direct. It could include 
any personal detail that can be used to identify an individual. Examples
 of this kind of PII include:

- Full name
- Home address
- Email address
- Social security number
- Passport number
- Driver’s license number
- Credit card numbers
- Date of birth
- Telephone number
- Owned properties e.g. vehicle identification number (VIN)
- Login details
- Processor or device serial number*
- Media access control (MAC)*
- Internet Protocol (IP) address*
- Device IDs*
- Cookies*

### **What is non-personal data?**

- Generalized data, e.i. age range e.g. 20-40
- Information gathered by government bodies or municipalities such as
census data or tax receipts collected for publicly funded works
- Aggregated statistics on the use of a product or service
- Partially or fully masked IP addresses

## **logging — Logging facility for Python**

The key benefit of having the logging API provided by a standard library module is that all Python modules can participate in logging, so your application log can include your own messages integrated with messages from third-party modules.

```python
# myapp.py
import logging
import mylib
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()
```

```python
# mylib.py
import logging
logger = logging.getLogger(__name__)

def do_something():
    logger.info('Doing something')
```

If you run *myapp.py*, you should see this in *myapp.log*:

```bash
INFO:__main__:Started
INFO:mylib:Doing something
INFO:__main__:Finished
```

## Regex using Re Module

**Compile the regular expression**: If you plan to use the same regex pattern multiple times, it's efficient to compile it into a regular expression object.
`pattern = re.compile(r'your_regex_pattern_here')`

Replace `'your_regex_pattern_here'` with your actual regex pattern.

**Perform the matching**: There are several functions in the `re` module for matching patterns:

- `re.match(pattern, string)`: Checks for a match only at the beginning of the string.
- `re.search(pattern, string)`: Searches the entire string for a match.
- `re.findall(pattern, string)`: Finds all occurrences of the pattern in the string.
- `re.finditer(pattern, string)`: Returns an iterator yielding match objects over all non-overlapping matches for the pattern in the string.

```python
result = re.match(pattern, string)
# or
result = re.search(pattern, string)
# or
result = re.findall(pattern, string)
# or
result = re.finditer(pattern, string)
```

Replace `pattern` with your compiled regex pattern and `string` with the text you want to search within.

**Process the match result**: Depending on the function used, the match result will vary. Here are some common attributes and methods of match objects:

- `group()`: Returns the string matched by the regular expression.
- `start()`: Returns the starting index of the match.
- `end()`: Returns the ending index of the match.
- `span()`: Returns a tuple containing the (start, end) positions of the match.

```python
if result:
    print("Match found:", result.group())
```

**Modifiers and Flags**: You can use modifiers and flags to modify the behavior of the regular expression. For example, `re.IGNORECASE` can be used to perform case-insensitive matching.
`pattern = re.compile(r'your_regex_pattern_here', re.IGNORECASE)`
Remember to replace `'your_regex_pattern_here'` with your actual regex pattern.

**Common Regex Patterns**: Here are some common regex patterns:

- `\d`: Matches any decimal digit.
- `\w`: Matches any alphanumeric character plus underscore.
- `\s`: Matches any whitespace character.
- `.`: Matches any character except a newline.
- `[]`: Matches any single character within the brackets.
- ``, `+`, `?`, `{}`: Quantifiers to match zero or more, one or more, zero or one, or a specific number of occurrences respectively.

Source used: https://docs.python.org/3/library/re.html

## Using bcrypt Module to hash passwords

Using bcrypt to hash passwords is a recommended practice for securely storing passwords in a database. bcrypt is a password hashing function that incorporates a salt to protect against rainbow table attacks, which are precomputed tables used to crack password hashes.

```python
import bcrypt

# Hash a password
password = "example_password"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Check a password against a hash
entered_password = "example_password"
if bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password):
    print("Password is correct!")
else:
    print("Incorrect password.")
```

In this example:

- `bcrypt.hashpw()` is used to hash a password. It takes the password string encoded as bytes and a randomly generated salt (created by `bcrypt.gensalt()`). The resulting hash is a combination of the password and the salt.
- `bcrypt.checkpw()` is used to check whether a given password matches a stored hash. It takes the entered password, encodes it as bytes, and compares it against the stored hash.
