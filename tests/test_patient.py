"""Tests for the Patient model."""


def test_create_patient():
    """Check a patient is created correctly given a name."""
    from inflammation.models import Patient
    name = 'Alice'
    p = Patient(name=name)
    assert p.name == name

def test_add_patient_observation():
    """Check if observation for a patient is added correctly."""
    from inflammation.models import Patient
    name = 'Alice'
    p = Patient(name=name)
    day = 2
    value = 0.5
    assert p.add_observation(value).value == value
    assert p.add_observation(value, day).day == day

def test_patient_is_person():
    """Check if a patient is a person."""
    from inflammation.models import Patient, Person
    alice = Patient("Alice")
    assert isinstance(alice, Person)

def test_create_doctor():
    """Check a doctor is created correctly given a name."""
    from inflammation.models import Doctor
    name = 'Alice'
    p = Doctor(name=name)
    assert p.name == name

def test_doctor_is_person():
    """Check if a doctor is a person."""
    from inflammation.models import Doctor, Person
    doc = Doctor("Sheila Wheels")
    assert isinstance(doc, Person)

def test_add_patient_to_doctor():
    """Check patients are being added correctly by a doctor. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    new_patient = Patient("Bob")
    doc.add_patient(new_patient)
    assert doc.patients is not None
    assert len(doc.patients) == 1

def test_no_duplicate_patients():
    """Check adding the same patient to the same doctor twice does not result in duplicates. """
    from inflammation.models import Doctor, Patient
    doc = Doctor("Sheila Wheels")
    alice = Patient("Alice")
    doc.add_patient(alice)
    doc.add_patient(alice)
    assert len(doc.patients) == 1