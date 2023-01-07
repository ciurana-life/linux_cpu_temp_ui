import os


def cpu_temp() -> str:

    thermal_z_type = os.popen("cat /sys/class/thermal/thermal_zone*/type").read()
    thermal_z_temp = os.popen("cat /sys/class/thermal/thermal_zone*/temp").read()

    x86index = thermal_z_type.split("\n").index("x86_pkg_temp")
    thermal_temp = thermal_z_temp.split("\n")[x86index]

    return thermal_temp[:-3]
