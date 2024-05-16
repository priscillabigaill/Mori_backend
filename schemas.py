from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from typing_extensions import Annotated

# Create a type alias for the constrained string
PhoneStr = Annotated[str, constr(regex=r'^\+?1?\d{9,15}$')]

# User schemas
class UserBase(BaseModel):
    IDORole: int
    Email: str
    FullName: str
    Role: str

class UserCreate(UserBase):
    pass #ini harusnya ada password  

class UserSetPassword(BaseModel):
    Password: str

class UserUpdate(BaseModel):
    IDORole: Optional[str] = None
    Password: Optional[str] = None
    Email: Optional[str] = None
    FullName: Optional[str] = None
    Role: Optional[str] = None

class User(UserBase):
    UserID: int

    class Config:
        orm_mode = True

# ProcessedLeaves schemas
class ProcessedLeavesBase(BaseModel):
    Description: str
    FlouringID: str
    DryingID: str

class ProcessedLeavesCreate(ProcessedLeavesBase):
    pass

class ProcessedLeavesUpdate(BaseModel):
    Description: Optional[str] = None
    FlouringID: Optional[str] = None
    DryingID: Optional[str] = None

class ProcessedLeaves(ProcessedLeavesBase):
    ProductID: int

    class Config:
        orm_mode = True

# WetLeavesCollection schemas
class WetLeavesCollectionBase(BaseModel):
    UserID: int
    CentralID: int
    Date: str
    Time: str
    Weight: int
    Expired: bool
    ExpirationTime: str

class WetLeavesCollectionCreate(WetLeavesCollectionBase):
    pass

class WetLeavesCollectionUpdate(BaseModel):
    UserID: Optional[int] = None
    CentralID: Optional[int] = None
    Date: Optional[str] = None
    Time: Optional[str] = None
    Weight: Optional[int] = None
    Expired: Optional[bool] = None
    ExpirationTime: Optional[str] = None

class WetLeavesCollection(WetLeavesCollectionBase):
    WetLeavesBatchID: str

    class Config:
        orm_mode = True

# Centra Details
class CentraDetails(BaseModel):
    PIC_name: str
    location: str
    email: str
    phone: int
    drying_machine_status: str = None
    flouring_machine_status: str = None
    action: str = None

# DryingMachine schemas
class DryingMachineBase(BaseModel):
    Capacity: str

class DryingMachineCreate(DryingMachineBase):
    pass

class DryingMachineUpdate(BaseModel):
    Capacity: Optional[str] = None

class DryingMachine(DryingMachineBase):
    MachineID: str

    class Config:
        orm_mode = True

# DryingActivity schemas
class DryingActivityBase(BaseModel):
    UserID: int
    CentralID: int
    Date: str
    Weight: int
    DryingMachineID: str
    Time: str

class DryingActivityCreate(DryingActivityBase):
    pass

class DryingActivityUpdate(BaseModel):
    UserID: Optional[int] = None
    CentralID: Optional[int] = None
    Date: Optional[str] = None
    Weight: Optional[int] = None
    DryingMachineID: Optional[str] = None
    Time: Optional[str] = None

class DryingActivity(DryingActivityBase):
    DryingID: str

    class Config:
        orm_mode = True

# FlouringMachine schemas
class FlouringMachineBase(BaseModel):
    Capacity: str

class FlouringMachineCreate(FlouringMachineBase):
    pass

class FlouringMachineUpdate(BaseModel):
    Capacity: Optional[str] = None

class FlouringMachine(FlouringMachineBase):
    MachineID: str

    class Config:
        orm_mode = True

# FlouringActivity schemas
class FlouringActivityBase(BaseModel):
    UserID: int
    CentralID: int
    Date: str
    Weight: int
    FlouringMachineID: str
    DryingID: str

class FlouringActivityCreate(FlouringActivityBase):
    pass

class FlouringActivityUpdate(BaseModel):
    UserID: Optional[int] = None
    CentralID: Optional[int] = None
    Date: Optional[str] = None
    Weight: Optional[int] = None
    FlouringMachineID: Optional[str] = None
    DryingID: Optional[str] = None

class FlouringActivity(FlouringActivityBase):
    FlouringID: str

    class Config:
        orm_mode = True

# Centra schemas
class CentraBase(BaseModel):
    Address: str

class CentraCreate(CentraBase):
    pass

class CentraUpdate(BaseModel):
    Address: Optional[str] = None

class Centra(CentraBase):
    CentralID: int

    class Config:
        orm_mode = True

# Expedition schemas
class ExpeditionBase(BaseModel):
    EstimatedArrival: str
    TotalPackages: int
    ExpeditionDate: str
    ExpeditionServiceDetails: str
    Destination: str
    CentralID: int

class ExpeditionCreate(ExpeditionBase):
    pass

class ExpeditionUpdate(BaseModel):
    EstimatedArrival: Optional[str] = None
    TotalPackages: Optional[int] = None
    ExpeditionDate: Optional[str] = None
    ExpeditionServiceDetails: Optional[str] = None
    Destination: Optional[str] = None
    CentralID: Optional[int] = None

class Expedition(ExpeditionBase):
    ExpeditionID: int

    class Config:
        orm_mode = True

# ReceivedPackage schemas
class ReceivedPackageBase(BaseModel):
    ExpeditionID: int
    UserID: int
    PackageType: str
    ReceivedDate: str
    WarehouseDestination: str

class ReceivedPackageCreate(ReceivedPackageBase):
    pass

class ReceivedPackageUpdate(BaseModel):
    ExpeditionID: Optional[int] = None
    UserID: Optional[int] = None
    PackageType: Optional[str] = None
    ReceivedDate: Optional[str] = None
    WarehouseDestination: Optional[str] = None

class ReceivedPackage(ReceivedPackageBase):
    PackageID: int

    class Config:
        orm_mode = True

# PackageReceipt schemas
class PackageReceiptBase(BaseModel):
    UserID: int
    PackageID: int
    TotalWeight: int
    TimeAccepted: str
    Note: str
    Date: str

class PackageReceiptCreate(PackageReceiptBase):
    pass

class PackageReceiptUpdate(BaseModel):
    UserID: Optional[int] = None
    PackageID: Optional[int] = None
    TotalWeight: Optional[int] = None
    TimeAccepted: Optional[str] = None
    Note: Optional[str] = None
    Date: Optional[str] = None

class PackageReceipt(PackageReceiptBase):
    ReceiptID: int

    class Config:
        orm_mode = True

# Shipment
class ShipmentPickupSchedule(BaseModel):
    shipment_id: int
    pickup_time: datetime
    location: str

# ProductReceipt schemas
class ProductReceiptBase(BaseModel):
    ProductID: str
    ReceiptID: int
    RescaledWeight: int

class ProductReceiptCreate(ProductReceiptBase):
    pass

class ProductReceiptUpdate(BaseModel):
    ProductID: Optional[str] = None
    ReceiptID: Optional[int] = None
    RescaledWeight: Optional[int] = None

class ProductReceipt(ProductReceiptBase):
    ProductReceiptID: int

    class Config:
        orm_mode = True

# PackageType schemas
class PackageTypeBase(BaseModel):
    Description: str

class PackageTypeCreate(PackageTypeBase):
    pass

class PackageTypeUpdate(BaseModel):
    Description: Optional[str] = None

class PackageType(PackageTypeBase):
    PackageTypeID: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, EmailStr, constr

class HarborGuardBase(BaseModel):
    PIC_name: str
    email: EmailStr
    phone: Optional[PhoneStr] = None

class HarborGuardCreate(HarborGuardBase):
    """
    All fields are required when creating a new harbor guard.
    """
    pass

class HarborGuardUpdate(HarborGuardBase):
    """
    All fields are optional for update operations.
    """
    PIC_name: str = None
    email: EmailStr = None
    phone: Optional[PhoneStr] = None

class HarborGuard(HarborGuardBase):
    """
    This class can be used to represent the harbor guard with additional fields if necessary,
    such as an internal ID or other attributes that are generated by the database.
    """
    id: int  # Assuming an 'id' field is automatically generated by the database

    class Config:
        orm_mode = True  # This setting is crucial for compatibility with ORMs like SQLAlchemy

# WAREHOUSE LOCATION
class WarehouseBase(BaseModel):
    PIC_name: str
    email: EmailStr
    phone: Optional[PhoneStr] = None

class WarehouseCreate(WarehouseBase):
    pass

class WarehouseUpdate(BaseModel):
    PIC_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[PhoneStr] = None

class Warehouse(WarehouseBase):
    id: int  # Assuming an 'id' field is automatically generated by the database

    class Config:
        orm_mode = True  # This setting is crucial for compatibility with ORMs like SQLAlchemy

# User (Admin)
class UserBase(BaseModel):
    PIC_name: str
    email: EmailStr
    phone: Optional[PhoneStr] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    PIC_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[PhoneStr] = None

class User(UserBase):
    id: int  # Assuming an 'id' field is automatically generated by the database

    class Config:
        orm_mode = True  # This setting is crucial for compatibility with ORMs like SQLAlchemy

