def as_dict(cls) -> dict[str, str]:
    """Return a dictionary of event names and values."""
    return {member.name: member.value for member in cls}