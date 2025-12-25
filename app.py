from core.infrastructure import InfrastructureManager

infra = InfrastructureManager()

if infra.wake_up_brain():
    pass
else:
    print("Dừng chương trình. Kiểm tra lại nguồn điện Workstation!")