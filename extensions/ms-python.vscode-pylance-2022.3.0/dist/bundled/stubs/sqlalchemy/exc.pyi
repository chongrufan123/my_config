from typing import Any, Optional

class SQLAlchemyError(Exception):
    code: Optional[str] = ...
class ArgumentError(SQLAlchemyError): ...

class ObjectNotExecutableError(ArgumentError):
    def __init__(self, target) -> None: ...

class NoSuchModuleError(ArgumentError): ...
class NoForeignKeysError(ArgumentError): ...
class AmbiguousForeignKeysError(ArgumentError): ...

class CircularDependencyError(SQLAlchemyError):
    cycles: Any = ...
    edges: Any = ...
    def __init__(self, message, cycles, edges, msg: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...

class CompileError(SQLAlchemyError): ...

class UnsupportedCompilationError(CompileError):
    def __init__(self, compiler, element_type) -> None: ...

class IdentifierError(SQLAlchemyError): ...
class DisconnectionError(SQLAlchemyError):
    invalidate_pool: bool = ...
class InvalidatePoolError(DisconnectionError): ...
class TimeoutError(SQLAlchemyError): ...
class InvalidRequestError(SQLAlchemyError): ...
class NoInspectionAvailable(InvalidRequestError): ...
class ResourceClosedError(InvalidRequestError): ...
class NoSuchColumnError(KeyError, InvalidRequestError): ...
class NoReferenceError(InvalidRequestError): ...

class NoReferencedTableError(NoReferenceError):
    table_name: str = ...
    def __init__(self, message, tname) -> None: ...
    def __reduce__(self): ...

class NoReferencedColumnError(NoReferenceError):
    table_name: str = ...
    column_name: str = ...
    def __init__(self, message, tname, cname) -> None: ...
    def __reduce__(self): ...

class NoSuchTableError(InvalidRequestError): ...
class UnboundExecutionError(InvalidRequestError): ...
class DontWrapMixin(object): ...

UnmappedColumnError: Any

class StatementError(SQLAlchemyError):
    statement: Any = ...
    params: Any = ...
    orig: Any = ...
    detail: Any = ...
    def __init__(self, message, statement, params, orig) -> None: ...
    def add_detail(self, msg): ...
    def __reduce__(self): ...
    def __unicode__(self): ...

class DBAPIError(StatementError):
    @classmethod
    def instance(cls, statement, params, orig, dbapi_base_err, connection_invalidated: bool = ...,
                 dialect: Optional[Any] = ...): ...
    def __reduce__(self): ...
    connection_invalidated: Any = ...
    def __init__(self, statement, params, orig, connection_invalidated: bool = ...) -> None: ...

class InterfaceError(DBAPIError): ...
class DatabaseError(DBAPIError): ...
class DataError(DatabaseError): ...
class OperationalError(DatabaseError): ...
class IntegrityError(DatabaseError): ...
class InternalError(DatabaseError): ...
class ProgrammingError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...
class SADeprecationWarning(DeprecationWarning): ...
class SAPendingDeprecationWarning(PendingDeprecationWarning): ...
class SAWarning(RuntimeWarning): ...
