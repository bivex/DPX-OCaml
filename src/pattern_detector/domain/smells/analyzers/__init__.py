"""Clean Code Smell Analyzers package."""

from pattern_detector.domain.smells.analyzers.architecture_analyzer import (
    ArchitectureSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.base import BaseSmellAnalyzer
from pattern_detector.domain.smells.analyzers.control_flow_analyzer import (
    ControlFlowSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.dependencies_analyzer import (
    DependenciesSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.duplication_analyzer import (
    DuplicationSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.error_handling_analyzer import (
    ErrorHandlingSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.functions_analyzer import (
    FunctionsSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.modules_analyzer import (
    ModulesSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.naming_analyzer import (
    NamingSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.refactoring_safety_analyzer import (
    RefactoringSafetySmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.state_effects_analyzer import (
    StateAndEffectsSmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.testability_analyzer import (
    TestabilitySmellAnalyzer,
)
from pattern_detector.domain.smells.analyzers.types_analyzer import (
    TypesSmellAnalyzer,
)

ALL_SMELL_ANALYZERS: list[BaseSmellAnalyzer] = [
    FunctionsSmellAnalyzer(),
    NamingSmellAnalyzer(),
    TypesSmellAnalyzer(),
    ControlFlowSmellAnalyzer(),
    ModulesSmellAnalyzer(),
    DuplicationSmellAnalyzer(),
    StateAndEffectsSmellAnalyzer(),
    DependenciesSmellAnalyzer(),
    ErrorHandlingSmellAnalyzer(),
    TestabilitySmellAnalyzer(),
    ArchitectureSmellAnalyzer(),
    RefactoringSafetySmellAnalyzer(),
]

__all__ = [
    "ALL_SMELL_ANALYZERS",
    "ArchitectureSmellAnalyzer",
    "BaseSmellAnalyzer",
    "ControlFlowSmellAnalyzer",
    "DependenciesSmellAnalyzer",
    "DuplicationSmellAnalyzer",
    "ErrorHandlingSmellAnalyzer",
    "FunctionsSmellAnalyzer",
    "ModulesSmellAnalyzer",
    "NamingSmellAnalyzer",
    "RefactoringSafetySmellAnalyzer",
    "StateAndEffectsSmellAnalyzer",
    "TestabilitySmellAnalyzer",
    "TypesSmellAnalyzer",
]
