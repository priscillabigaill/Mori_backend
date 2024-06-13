from typing import Optional
from pydantic import BaseModel, EmailStr, constr, ValidationError, Field
from datetime import datetime, date, time
from typing_extensions import Annotated
import re

# user schemas
class UserBase(BaseModel):
    IDORole: Optional[int] = None
    Email: EmailStr
    FullName: str
    Role: str
    Phone: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    IDORole: Optional[str] = None
    Password: Optional[str] = None
    Email: Optional[str] = None
    FullName: Optional[str] = None
    Role: Optional[str] = None
    Phone: Optional[str] = None

class UserSetPassword(BaseModel):
    token: str
    new_password: str
  

class User(UserBase):
    UserID: int

    class Config:
        from_attributes = True

class UserRegistration(BaseModel):
    Email: str
    FullName: str
    Role: str
    Password: str


class UserLogin(BaseModel):
    Email: str
    Password: str
    


class UserVerification(BaseModel):
    Email:str
    Code: str

# User (Admin)
class AdminBase(BaseModel):
    PIC_name: str
    email: EmailStr
    phone: Optional[str] = None

class AdminCreate(AdminBase):
    pass

class AdminUpdate(BaseModel):
    PIC_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class Admin(AdminBase):
    id: int  # Assuming an 'id' field is automatically generated by the database

    class Config:
        from_attributes = True  # This setting is crucial for compatibility with ORMs like SQLAlchemy

# ProcessedLeaves schemas
class ProcessedLeavesBase(BaseModel):
    # ProductID: int
    Description: Optional[str] = None
    DryingID: Optional[int] = None
    FlouringID: Optional[int] = None
    DriedDate: date
    FlouredDate: date

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
    
    # UserID: int
    CentralID: int
    Date: datetime
    Weight: int
    Expired: bool
    ExpirationTime: time

class WetLeavesCollectionCreate(WetLeavesCollectionBase):
    pass

class WetLeavesCollectionUpdate(BaseModel):
    # UserID: Optional[int] = None
    # CentralID: Optional[int] = None
    # WetLeavesBatchID: Optional[str] = None
    Date: Optional[datetime] = None
    Weight: Optional[int] = None
    Expired: Optional[bool] = None
    ExpirationTime: Optional[time] = None

class WetLeavesCollection(WetLeavesCollectionBase):
    WetLeavesBatchID: int

    class Config:
        orm_mode = True

# Centra Details
class CentraBase(BaseModel):
    Address: str

class CentraCreate(CentraBase):
    pass

class CentraDetails(CentraBase):
    CentralID: int

    class Config: 
        orm_mode = True

# DryingMachine schemas
class DryingMachineBase(BaseModel):
    Capacity: str
    Status: str

class DryingMachineCreate(DryingMachineBase):
    pass

class DryingMachineUpdate(BaseModel):
    Capacity: Optional[str] = None

class DryingMachine(DryingMachineBase):
    MachineID: int

    class Config:
        orm_mode = True

# DryingActivity schemas
class DryingActivityBase(BaseModel):
    CentralID: int
    Date: date
    Weight: int
    DryingMachineID: int
    Time: time

class DryingActivityCreate(DryingActivityBase):
    pass

class DryingActivityUpdate(BaseModel):
    DryingID: Optional[int] = None
    UserID: Optional[int] = None
    CentralID: Optional[int] = None
    Date: Optional[date] = None
    Weight: Optional[int] = None
    DryingMachineID: Optional[str] = None
    Time: Optional[time] = None

class DryingActivity(DryingActivityBase):
    DryingID: int

    class Config:
        orm_mode = True

# FlouringMachine schemas
class FlouringMachineBase(BaseModel):
    Capacity: str
    Status: str

class FlouringMachineCreate(FlouringMachineBase):
    pass

class FlouringMachineUpdate(BaseModel):
    Capacity: Optional[str] = None

class FlouringMachine(FlouringMachineBase):
    MachineID: int

    class Config:
        orm_mode = True

# FlouringActivity schemas
class FlouringActivityBase(BaseModel):
    CentralID: Optional[int] = None
    Date: Optional[date] = None
    Weight: Optional[int] = None
    FlouringMachineID: Optional[int] = None
    Time: Optional[time] = None

class FlouringActivityCreate(FlouringActivityBase):
    pass

class FlouringActivityUpdate(BaseModel):
    FlouringID: Optional[int] = None
    UserID: Optional[int] = None
    CentralID: Optional[int] = None
    Date: Optional[date] = None
    Weight: Optional[int] = None
    FlouringMachineID: Optional[int] = None
    # DryingID: Optional[str] = None
    Time: Optional[time] = None

class FlouringActivity(FlouringActivityBase):
    FlouringID: int

    class Config:
        orm_mode = True

#stocks
class StockBase(BaseModel):
    product_id: int
    weight: int

class StockCreate(StockBase):
    pass

class StockUpdate(StockBase):
    pass

class Stock(StockBase):
    id: int
    location_id: Optional[int] = None

    class Config:
        from_attributes = True

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
        from_attributes = True

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
        from_attributes = True

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
        from_attributes = True

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
        from_attributes = True

# Shipment
class ShipmentPickupSchedule(BaseModel):
    # shipment_id: int
    pickup_time: datetime
    location: str

class ShipmentBase(BaseModel):
    batch_id: Optional[int] = None
    description: Optional[str] = None
    status: Optional[str] = None
    weight: Optional[float] = None
    issue_description: Optional[str] = None

class ShipmentCreate(ShipmentBase):
    pass

class ShipmentUpdate(BaseModel):
    shipment_id: Optional[int] = None
    batch_id: Optional[int] = None
    description: Optional[str] = None
    status: Optional[str] = None
    weight: Optional[int] = None
    issue_description: Optional[str] = None

class Shipment(ShipmentBase):
    shipment_id: int
    # created_at: Optional[datetime] = None
    # updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class ShipmentIssue(BaseModel):
    description: str

class ShipmentRescale(BaseModel):
    new_weight: float

class ShipmentConfirmation(BaseModel):
    weight: float

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
        from_attributes = True

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
        from_attributes = True

class HarborGuardBase(BaseModel):
    PIC_name: str
    email: EmailStr
    phone: Optional[str] = None

class HarborGuardCreate(HarborGuardBase):
    pass

class HarborGuardUpdate(HarborGuardBase):

    PIC_name: str = None
    email: EmailStr = None
    phone: Optional[str] = None

class HarborGuard(HarborGuardBase):
    HarborID: int  

    class Config:
        orm_mode = True  

# WAREHOUSE LOCATION
class WarehouseBase(BaseModel):
    PIC_name: str
    email: EmailStr
    phone: Optional[str] = None

class WarehouseCreate(WarehouseBase):
    pass

class WarehouseUpdate(BaseModel):
    PIC_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class Warehouse(WarehouseBase):
    id: int  # Assuming an 'id' field is automatically generated by the database

    class Config:
        from_attributes = True  # This setting is crucial for compatibility with ORMs like SQLAlchemy
