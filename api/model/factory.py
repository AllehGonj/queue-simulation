import random
import simpy

processes_flow_logs = []
lot_times = []


class Source:
    def __init__(self, env, attributes):
        self.env = env
        self.attributes = attributes

    def setup(self):
        global packs_count
        process = Factory(self.env, self.attributes, self.attributes.work_count)

        # Create initial fruit packages
        for packs_count in range(self.attributes.fruit_packs):
            self.start_process(packs_count, process)

        # Create more incoming packages while the simulation is running
        while True:
            arrival_interval = self.attributes.arrival_interval
            yield self.env.timeout(random.randint(arrival_interval - 30, arrival_interval + 30))
            packs_count += 1
            self.start_process(packs_count, process)

    def start_process(self, count, process):
        pack_name_identifier = 'Pack %d'
        pack = pack_name_identifier % count
        processes_flow_logs.append('%s arrives at the factory at %.2f.' % (pack, self.env.now))
        self.env.process(fruit_package(self.env, pack, process, target='preparation'))


class Factory(object):
    FLOW_LOGS_MESSAGE = '%s on %s station at %.2f.'

    def __init__(self, env, attributes, num_machines):
        self.env = env
        self.attributes = attributes
        self.machine = simpy.Resource(env, num_machines)

    def station(self, package: str, next_station: str, steps: list) -> None:
        if next_station is not None:
            self.env.process(fruit_package(self.env, package, self, target=next_station))

        yield self.env.timeout(self.attributes.times[steps[0]])
        processes_flow_logs.append(self.FLOW_LOGS_MESSAGE % (package, steps[0], self.env.now))

        yield self.env.timeout(self.attributes.times[steps[1]])
        processes_flow_logs.append(self.FLOW_LOGS_MESSAGE % (package, steps[1], self.env.now))


class FactoryLine(object):
    def __init__(self, steps, next_station=None):
        self.next_station = next_station
        self.steps = steps

    @classmethod
    def target_station(cls, target: str):
        processes = {
            'preparation': FactoryLine(['washing', 'desinfection'], 'cooking'),
            'cooking': FactoryLine(['pulping', 'cooking'], 'molding'),
            'molding': FactoryLine(['plucking', 'molding'], 'packing'),
            'packing': FactoryLine(['cutting', 'packing'], 'labeling'),
            'labeling': FactoryLine(['box_packing', 'labeling'])
        }
        line = processes.get(target, lambda: "Invalid process in fabric")
        return line


def fruit_package(env, name: str, process: Factory, target: str) -> None:
    with process.machine.request() as request:
        yield request
        line = FactoryLine.target_station(target)

        processes_flow_logs.append('%s enters the %s station at %.2f.' % (name, target, env.now))
        yield env.process(process.station(name, line.next_station, line.steps))
        processes_flow_logs.append('%s leaves the %s station at %.2f.' % (name, target, env.now))

        if line.next_station is None:
            lot_times.append(env.now)


def simulation(attrs) -> None:
    working_minutes_per_day = attrs.working_hours * 60
    random.seed(attrs.random_seed)

    # Create an environment and start the setup process
    env = simpy.Environment()
    env.process(Source(env, attrs).setup())

    # Execution
    env.run(until=attrs.working_days * working_minutes_per_day)
