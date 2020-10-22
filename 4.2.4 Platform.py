"""
Platform module, functions associated with it.
"""
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
print(platform())  # Returns a string like "Windosw-10-10.0.07763-SP0
print(platform(1))
print(platform(0, 1))

print(machine()) # Returns the name of processor. E.g. "AMD64"
print(processor()) # Returns the real processor name. E.g "Intel64 Family 6 Model..."
print(system()) # Returns the generic OS name as a string. E.g "windows".
print(version()) # Returns the OS version. E.g "10.0.17763

print(python_implementation()) # Returns the Python implementation, E.g. "CPython"
print(python_version_tuple()) # Returns ('3', '7', '0'), which is the python version.
for i in python_version_tuple(): # major, minor, and patch level number
    print(i)
