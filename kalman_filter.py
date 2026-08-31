class KalmanFilter1D:
    def __init__(self, initial_estimate, initial_uncertainty, process_variance, measurement_variance):
        self.estimate = initial_estimate
        self.uncertainty = initial_uncertainty
        self.process_variance = process_variance
        self.measurement_variance = measurement_variance

    def predict(self):
        self.uncertainty = self.uncertainty + self.process_variance

    def update(self, measurement):
        kalman_gain = self.uncertainty / (self.uncertainty + self.measurement_variance)
        self.estimate = self.estimate + kalman_gain * (measurement - self.estimate)
        self.uncertainty = (1 - kalman_gain) * self.uncertainty
        return self.estimate

    def filter(self, measurement):
        self.predict()
        return self.update(measurement)
