import copy


class CGlobalState:
    def __init__(self):
        self._descriptors = dict
        self._name = ""

    def copyInstance(self, instance):
        if isinstance(instance, self.__class__):
            copiedInstance = copy.deepcopy(instance)

            self.setName(copiedInstance.getName())

            for key, value in copiedInstance.getDescriptors().items():
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
        self._descriptors = copy.deepcopy(descriptors)

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
        # TODO consult with thesis supervisor
        identical = True
        state = copy.deepcopy(state)
        attributes = copy.deepcopy(attributes)
        size = attributes.size()

        for i in range(size):
            if attributes.test(i):
                descriptorClassValue = self.getDescriptors().get(i)
                descriptorStateValue = state.getDescriptors().get(i)
                if descriptorClassValue != descriptorStateValue:
                    identical = False
                    break
        return identical

    def compareUsingAttribute(self, state, attribute):
        # TODO consult with thesis supervisor
        descriptorClassValue = self.getDescriptors().get(attribute)
        descriptorStateValue = state.getDescriptors().get(attribute)

        return descriptorClassValue == descriptorStateValue

    def assignOperator(self, globalState):
        if isinstance(globalState, self.__class__):
            copiedInstance = copy.deepcopy(globalState)
            newGlobalStateInstance = CGlobalState()

            for key, value in copiedInstance.getDescriptors().items():
                self._descriptors[key] = value

            self.setName(copiedInstance.getName())

            newGlobalStateInstance.setDescriptors(self._descriptors)
            newGlobalStateInstance.setName(self._name)

            return newGlobalStateInstance
        else:
            raise ValueError(globalState)

    def comparasionOperator(self, globalState):
        if isinstance(globalState, self.__class__):

            copiedInstance = copy.deepcopy(globalState)
            classDescriptors = self._descriptors
            instanceDescriptors = copiedInstance.getDescriptors()

            equal = True

            for keyDescriptor, keyInstance in zip(classDescriptors.keys(), instanceDescriptors.keys()):
                if classDescriptors[keyDescriptor] != instanceDescriptors[keyInstance]:
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
