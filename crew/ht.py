class NoiseFilter:
    def __init__(self):
        self.class_counter = {}
        self.noise_threshold = 50  # Adjustable

    def track_classes(self, attrs):
        for key, val in attrs:
            if key == 'class':
                for cls in val.split():
                    self.class_counter[cls] = self.class_counter.get(cls, 0) + 1

    def is_noisy_class(self, cls):
        return self.class_counter.get(cls, 0) > self.noise_threshold

    def clean_attrs(self, attrs):
        cleaned = []
        for key, val in attrs:
            if key == 'class':
                filtered = [c for c in val.split() if not self.is_noisy_class(c)]
                if filtered:
                    cleaned.append((key, ' '.join(filtered)))
            elif key not in ['style', 'data-*', 'aria-*']:
                cleaned.append((key, val))
        return cleaned

    def is_noise_tag(self, tag):
        return tag in ['svg', 'path', 'script', 'style', 'meta', 'link']
