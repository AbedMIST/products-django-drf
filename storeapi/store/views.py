from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema
from .models import Store
from .serializers import StoreSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def getStores(request):
    """Retrieve all stores (public)"""
    stores = Store.objects.all()
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def storeDetail(request, pk):
    """Get store details with products (public)"""
    try:
        store = Store.objects.get(id=pk)
    except Store.DoesNotExist:
        return Response(
            {"error": "Store not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = StoreSerializer(store)
    return Response(serializer.data)


@extend_schema(
    request=StoreSerializer,
    responses={201: StoreSerializer},
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addStore(request):
    """Create a new store (requires JWT token)"""
    serializer = StoreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    request=StoreSerializer,
    responses={200: StoreSerializer},
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateStore(request, pk):
    """Update store (requires JWT token)"""
    try:
        store = Store.objects.get(id=pk)
    except Store.DoesNotExist:
        return Response(
            {"error": "Store not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = StoreSerializer(store, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteStore(request, pk):
    """Delete store (requires JWT token)"""
    try:
        store = Store.objects.get(id=pk)
    except Store.DoesNotExist:
        return Response(
            {"error": "Store not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    store.delete()
    return Response({"message": "Store deleted"}, status=status.HTTP_204_NO_CONTENT)