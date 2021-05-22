import asyncio
import sys

import cozmo


async def cozmo_program(robot: cozmo.robot.Robot):

    while(True):
        try:
            tapped = await robot.world.wait_for(cozmo.objects.EvtObjectTapped)

            print(tapped.tap_duration)

            if tapped.tap_intensity < 100:
                lights = cozmo.lights.green_light
            elif tapped.tap_intensity < 140:
                lights = cozmo.lights.blue_light
            else:
                lights = cozmo.lights.red_light

            cube = tapped.obj
            cube.set_light_corners(lights, lights, lights, lights)

        except asyncio.TimeoutError:
            print("Didn't find a cube :-(")
            return


cozmo.run_program(cozmo_program)
