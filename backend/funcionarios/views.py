from django.http import Http404

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FuncionarioSerializer
from .models import Funcionario


class FuncionariosCrud(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get_object(pk):
        try:
            return Funcionario.objects.get(pk=pk, ativo=True)
        except Funcionario.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        produto = self.get_object(pk)
        serializer = FuncionarioSerializer(produto)
        return Response(serializer.data)

    def put(self, request, pk):
        produto = self.get_object(pk)
        serializer = FuncionarioSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        produto = self.get_object(pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FuncionariosListPost(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Funcionario.objects.filter(ativo=True).all()
    serializer_class = FuncionarioSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
