

class SampleExercise():
    def __init__(self, name='', description='', sets=0, reps=0, config_options=[], notes=''):
        self.name = name
        self.description = description
        self.reps = reps
        self.sets = sets
        self.configuration_units = config_options
        self.notes = notes

    def rep_string(self):
        s = ''
        if self.sets:
            s += f'{self.sets} sets'
            if self.reps:
                s += ' of '
        if self.reps:
            s += f'{self.reps} reps'

        return s

    def add_config(self, config_options):
        self.configuration_units.append(config_options)


leg_stretch = SampleExercise(
        name='Calf stretch',
        description='Warm up the legs',
        notes="legsercise am i rite"
    )
arm_stretch = SampleExercise(
        name='Shoulder Roll',
        description='Stretches the chest and back muscles',
        notes="sushi joke goes here"
    )

punching_bag = SampleExercise(
        name='Punching Bag',
        description='Punching a bag',
        notes="Give em the ol' 1-2"
    )
rowing_machine = SampleExercise(
        name='Rowing Machine',
        description='Simulated boat rowing on a machine',
        notes='Rowing machines vary'
    )

bodyweight_squats = SampleExercise(
        name='Bodyweight Squats',
        description='Just like barbell front squats but without the barbell',
        notes="squats 4 teh th0ts"
    )
push_ups = SampleExercise(
        name='Push Ups',
        description='A horizontal press motion with bodyweight',
        notes="SCAPULAR ROTATION"
    )

deadlift = SampleExercise(
        name='Deadlift',
        description='Lifting a barbell from the ground to hip height',
        notes=""
    )
overhead_press = SampleExercise(
        name='Overhead Press',
        description='Vertical barbell press that should have been called the push up',
        notes="aka strict press, aka military press"
    )

sample_exercises = [
    leg_stretch,arm_stretch,
    punching_bag,rowing_machine,
    bodyweight_squats,push_ups,
    deadlift,overhead_press
]


class ExerciseConfigOption():
    def __init__(self, name='', unit_type='', value=0, behavior=''):
        self.name=name
        self.unit_type=unit_type
        self.value=value
        self.behavior = behavior


cfg_pounds = ExerciseConfigOption(
    name='Pounds',
    unit_type='weight',
)
cfg_miles = ExerciseConfigOption(
    name='Miles',
    unit_type='distance',
)
cfg_seconds = ExerciseConfigOption(
    name='Seconds',
    unit_type='duration',
)


class ExerciseGroup():
    def __init__(self, name='', exercises=[], reps=1, tag_groups=[]):
        self.name=name
        self.exercises=exercises
        self.reps = reps
        self.tag_groups=tag_groups


sample_warmup = ExerciseGroup(
    name='Generic Warmup',
    exercises=[
        SampleExercise(
            name='Hamstring stretch',
            description='Warm up the legs',
            reps=2,
            config_options=[
                ExerciseConfigOption(
                    name='Seconds',
                    value=60
                )
            ],
            notes="legsercise am i rite"
        ),
        SampleExercise(
            name='Shoulder Roll',
            description='Stretches the chest and back muscles',
            reps=10,
            notes="sushi joke goes here"
        ),


        SampleExercise(
            name='Rowing Machine',
            description='Simulated boat rowing on a machine',
            reps=1,
            config_options=[
                ExerciseConfigOption(
                    name='Miles',
                    value=0.25
                )
            ],
            notes='Rowing machines vary',
        )
    ]
)


sample_working_set = ExerciseGroup(
    name='Generic Working Set',
    exercises=[
        SampleExercise(
            name='Bodyweight Squats',
            description='the normal description for bodyweight squats',
            reps=10,
            notes="legsercise am i rite"
        ),
        SampleExercise(
            name='Kettlebell Swings',
            description='Hinging at the hips to swing the kettlebell from under the legs to shoulder height',
            reps=20,
            config_options=[
                ExerciseConfigOption(
                    name='Pounds',
                    value=20
                )
            ],
            notes="Hip Drahve"
        ),
    ]
)
sample_cooldown = ExerciseGroup(
    name='Generic Cooldown',
    exercises=[
        SampleExercise(
            name='Hamstring stretch',
            description='Warm up the legs',
            reps=2,
            config_options=[
                ExerciseConfigOption(
                    name='Seconds',
                    value=60
                )
            ],
            notes="legsercise am i rite"
        )
    ]
)

sample_exercise_groups = [
    sample_warmup,
    sample_working_set,
    sample_cooldown
]


class Workout:
    def __init__(self, name='', exercise_groups=[],notes=''):
        self.name=name
        self.exercise_groups=exercise_groups
        self.notes=notes


sample_workout = Workout(
    name='demo workout',
    exercise_groups=[
        sample_warmup,
        sample_working_set,
        sample_cooldown
    ]
)

sample_workouts = [
    sample_workout
]


class WorkoutDay:
    def __init__(self, name, workouts=[], rest_day=False):
        self.name = name
        self.workouts = workouts
        self.is_rest_day = rest_day


sample_workout_day_one = WorkoutDay(name="day 1", workouts=sample_workouts)
sample_workout_day_two = WorkoutDay(name="day 2", workouts=sample_workouts)
sample_workout_day_three = WorkoutDay(name="day 3", workouts=sample_workouts)
sample_rest_day = WorkoutDay(name="Rest Day", rest_day=True)


class WorkoutSchedule:
    def __init__(self, name, days=[]):
        self.name = name
        self.days = days


sample_workout_schedule = WorkoutSchedule(name="Demo Schedule", days = [
    sample_workout_day_one,
    sample_rest_day,
    sample_workout_day_two,
    sample_rest_day,
    sample_workout_day_three
])


class TrainingTrack:
    def __init__(self, name, description='', schedules=[]):
        self.name = name
        self.description = description
        self.schedules = schedules

    def days(self):
        days = 0
        for s in self.schedules:
            days += len(s.days)
        return days

sample_training_track = [TrainingTrack(name="Demo Training Track", schedules=[sample_workout_schedule],
                                  description="30 days to sick abs or something")]
