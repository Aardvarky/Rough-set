import copy
from HashableDict import HashableDict


class CGlobalState:
    def __init__(self):
        self._name = ""
        self._descriptors = HashableDict()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if other.getDescriptors() == self.getDescriptors():
                return True
            else:
                return False
        else:
            return False

    def __hash__(self):
        return hash(frozenset(self._descriptors.items()))

    def copyInstance(self, instance):
        if isinstance(instance, self.__class__):
            self.setName(instance.getName())

            for key, value in instance.getDescriptors().items():
                self._descriptors[key] = value
        else:
            raise ValueError(instance)

    def addDescriptor(self, attribute, value):
        if type(attribute) == int and type(value) == float:
            self._descriptors[attribute] = value
        else:
            raise ValueError(attribute, value)

    def getAttributeValue(self, attribute):
        return self._descriptors[attribute]

    def getDescriptors(self):
        return self._descriptors

    def setDescriptors(self, descriptors):
        self._descriptors = descriptors

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def compareUsingAttributesList(self, state, attributes):
        identical = True

        for i in range(len(attributes)):
            descriptorClassValue = self.getDescriptors().get(attributes[i])
            descriptorStateValue = state.getDescriptors().get(attributes[i])
            if descriptorClassValue != descriptorStateValue:
                identical = False
                break
        return identical

    def compareUsingBitset(self, state, attributes):
        identical = True

        for i in range(attributes.size()):
            if attributes.test(i):
                value = self.getDescriptors().get(i)
                value1 = state.getDescriptors().get(i)

                if value != value1:
                    identical = False
                    break
        return identical

    def compareUsingAttribute(self, state, attribute):
        descriptorClassValue = self.getDescriptors().get(attribute)
        descriptorStateValue = state.getDescriptors().get(attribute)

        return descriptorClassValue == descriptorStateValue

    def assignOperator(self, globalState):
        if isinstance(globalState, self.__class__):
            newGlobalState = CGlobalState()

            for key, value in globalState.getDescriptors().items():
                self._descriptors.add(key, value)
                # self._descriptors[key] = value
            self.setName(globalState.getName())

            newGlobalState.setDescriptors(self._descriptors)
            newGlobalState.setName(self._name)

            return newGlobalState
        else:
            raise ValueError(globalState)

    def comparasionOperator(self, globalState):
        if isinstance(globalState, self.__class__):

            copiedInstance = copy.deepcopy(globalState)
            classDescriptors = self._descriptors
            instanceDescriptors = copiedInstance.getDescriptors()

            equal = True

            for keyDescriptor, keyInstance in zip(classDescriptors.keys(), instanceDescriptors.keys()):
                if classDescriptors.get(keyDescriptor) != instanceDescriptors.get(keyInstance):
                    equal = False
                    break
            return equal
        else:
            raise ValueError(globalState)

    def read(self, pObjectNode, attributeNameOfName, attributeTypes, Entr):
        pass

    def loadFromProject(self):
        pass

    def saveToProject(self):
        pass

    def saveTinyXML(self):
        pass
